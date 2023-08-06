""" Model """

from prompt import generate_prompt_few_shot
from peft import PeftModel
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, GenerationConfig
from typing import List
import settings
import torch


class GenerativeModel:
    def load_model(self):
        peft_model_base = AutoModelForSeq2SeqLM.from_pretrained(
            settings.BASE_MODEL, torch_dtype=torch.bfloat16
        )
        self.tokenizer = AutoTokenizer.from_pretrained(settings.BASE_MODEL)
        self.model = PeftModel.from_pretrained(
            peft_model_base,
            settings.PEFT_MODEL,
            torch_dtype=torch.bfloat16,
            is_trainable=False,
        )
        return self

    def generate_response(self, comment: str) -> List[str]:
        prompt = generate_prompt_few_shot(comment)
        inputs = self.tokenizer(prompt, return_tensors="pt")
        output_ids = self.model.generate(
            input_ids=inputs["input_ids"],
            generation_config=GenerationConfig(
                max_new_tokens=settings.MAX_NEW_TOKENS,
                do_sample=settings.DO_SAMPLE,
                temperature=settings.TEMPRATURE,
                num_return_sequences=settings.NUM_RETURN_SEQUENCE,
            ),
        )
        responses = [
            self.tokenizer.decode(ids, skip_special_tokens=True) for ids in output_ids
        ]

        return responses
