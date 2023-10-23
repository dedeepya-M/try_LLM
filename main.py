from langchain.llms import OpenAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
load_dotenv()

def generate_name(Type,color):
    llm = OpenAI(
        temperature = 0.5
    )
    prompt_template = PromptTemplate(
        input_variables = ['Type','color'],
        template =  "I have a {Type} {color} desk and I want few decoration ideas for it"
    )
    chain = LLMChain(llm=llm,prompt = prompt_template)
    response = chain({'Type':Type,'color':color})
    return response

if __name__ == "__main__":
    print(generate_name("wooden","black"))