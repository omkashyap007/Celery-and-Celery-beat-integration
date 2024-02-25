NEWS_API_ORG_API_KEY = "67faf78c749f48878d445f380d65e019"

NEWS_API_TOP_HEADLINES_GET_REQUEST = {
    "url" : "https://newsapi.org/v2/top-headlines/" ,
    "parameters" : {
        "country" : "in" , 
        "category" : "sports" , 
        "apiKey" : NEWS_API_ORG_API_KEY , 
    }
}
NEWS_API_EVERYTHING_GET_REQUEST = {
    "url" : "https://newsapi.org/v2/everything/" ,
    "parameters" : {
        "q" : "AI" , 
        "apiKey" : NEWS_API_ORG_API_KEY , 
    }
}