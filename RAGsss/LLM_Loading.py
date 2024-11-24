from langchain.llms import HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from huggingface_hub import login

login(token="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")


def load_llama_model(model_name: str = "meta-llama/Llama-2-7b-hf", device: str = "cpu"):
    """
    Load a free and open-source LLaMA model from Hugging Face.
    :param model_name: The model name to load.
    :param device: Device to use for inference ("cuda" or "cpu").
    :return: A LangChain-compatible LLM instance.
    """
    # Load the tokenizer and model from Hugging Face
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")

    # Create a text generation pipeline
    generation_pipeline = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        device=0 if device == "cuda" else -1,
        max_length=1024,
        temperature=0.7,
        top_p=0.9,
    )

    # Wrap the pipeline in a LangChain-compatible LLM
    llm = HuggingFacePipeline(pipeline=generation_pipeline)
    return llm
