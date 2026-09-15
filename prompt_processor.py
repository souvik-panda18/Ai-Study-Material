if __name__ == "__main__":
    prompts = [
    "Explain machine learning",
    "Explain RAG",
    "Explain transformers",
    "Explain embeddings"]
    def cleanprompt(prompt):
        return prompt.strip().lower()

    def tagPrompt(prompt):
        cleaned_prompt = cleanprompt(prompt)
        if "machine learning" in cleaned_prompt:
            return "ML"
        elif "rag" in cleaned_prompt:
            return "RAG"
        elif "transformers" in cleaned_prompt:
            return "Transformers"
        elif "embeddings" in cleaned_prompt:
            return "Embeddings"
        else:
            return "Unknown"

    def buildPromptDic(prompt):
        tag = tagPrompt(prompt)
        prompt = cleanprompt(prompt)
        dict1={"prompt": prompt,
            "tag": tag,
            "Length": len(prompt)}
        return dict1

# filter_by_length — takes a list of dictionaries, returns a filtered list
    def filter_by_length(prompt_dicts, min_length):
        return [d for d in prompt_dicts if d["Length"] >= min_length]
    def sortByLen(prompt_dicts):
        return sorted(prompt_dicts, key=lambda x: x["Length"])

# prompt_generator — takes the raw list, yields processed dictionaries one at a time
    def prompt_generator(prompts):
        for prompt in prompts:
            yield buildPromptDic(prompt)


#list to collect data from prompt_generator
    prompt_data = list(prompt_generator(prompts))

# filter the list of dictionaries by length
    filtered_prompts = filter_by_length(prompt_data, 100)

    sort = sortByLen(filtered_prompts)

#Prints the final result — a loop with print() per dictionary is more readable than printing the whole list at once
    res = [print(d) for d in sort]