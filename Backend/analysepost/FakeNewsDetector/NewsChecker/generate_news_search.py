import os
import time
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from .generate_news_search_specs import NewsSearchGeneratorSpecs
load_dotenv()

def NewsSearchGenerator(news_entities,model):
    llm=model.with_structured_output(NewsSearchGeneratorSpecs)
    template="""
    You are given a list of entities.
    You have to generate 3 search queries related to those entities to get news about them on search engine.
    **Note**: 
     -A search query should not be more than 10-12 words.
     - Have the correlation between entities in the search query.
    Entities:
    {entities}
    """


    prompt=ChatPromptTemplate.from_template(template=template,input_variable=["entities"])
    news_search_gen_chain=prompt|llm
    news_query=news_search_gen_chain.invoke({"entities":news_entities}).news_search_query
    print("News Search Query generated....")
    time.sleep(5)

    return news_query


if __name__=="__main__":
    entities=['Delhi Railway station', '18 dead', 'several injured']
    news_query=NewsSearchGenerator(entities)
    print(news_query)

