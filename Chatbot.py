# Importing requiered tools from transformers library
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Choosing a model
# Here, we'll be using "facebook/blenderbot-400M-distill" because it has an open-source license and runs relatively fast.
model_name = "facebook/blenderbot-400M-distill"

# Fetch the model and initialize a tokenizer
# Load model (download on first run and reference local installation for consequent runs)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Keeping track of conversation history
conversation_history = []

while True:
    # Encoding the conversation history
    history_string = "\n".join(conversation_history)

    # Fetch prompt from user
    input_text ="Hello?"

    # Tokenization of user prompt and chat history
    inputs = tokenizer.encode_plus(history_string, input_text, return_tensors="pt")
    print(inputs)

    tokenizer.pretrained_vocab_files_map

    # Generate output from the model
    outputs = model.generate(**inputs)
    print(outputs)

    # Decode output
    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
    print(response)

    # Update conversation history
    conversation_history.append(input_text)
    conversation_history.append(response)
    print(conversation_history)