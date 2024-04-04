prompt_v1 = """
Please provide a sentiment analysis for the following transcript. 
transcript : {context}
Analyze the emotions conveyed by the speakers and the overall tone of the conversation. 
Consider the use of language, tone, and any contextual cues to determine the sentiment expressed. 
Your analysis should include an assessment of both positive and negative sentiments present in the transcript.
"""

prompt_v2 = """
You are a sentiment analysis model. Your task is to analyze the context and determine the sentiment. Below provided is the context, which you are supposed to analyze and find the sentiment for:

Transcript: {context}

The provided transcript is from an audio file recorded during an interview, featuring a conversation between two speakers. One will act as the interviewer, and the other as the candidate. Your goal is to analyze the conversation and provide sentiment insights.

For each line of the conversation, please provide an analysis in the following format:

'[Speaker_Y] [sentiment_analysis_insight]'.

For example:

'[Speaker_1] likes a sport. It seems he cares about his health.'
'[Speaker_2] pretends to be smart.'

Your responses should focus solely on the sentiment or psychological insights derived from the conversation. Avoid providing summaries, keywords, or any other extraneous information.
"""

prompt_v3 = """
Input:
Please provide a transcript of a conversation between two speakers.

Task: 
Extract sentiment and psychological insights from the conversation transcript provided by the hiring manager. 
Please refrain from providing a summary or keywords. Focus solely on identifying sentiments and psychological traits 
exhibited by the speakers.

Transcript:
{context}

Instructions:
Listen to the provided conversation transcript, ensuring it involves at least two speakers engaged in a natural conversation.
Extract insights regarding the sentiments expressed by each speaker, focusing on their emotional tone, attitude, and demeanor.
Identify any psychological traits or tendencies exhibited by the speakers based on their dialogue, tone of voice, and mannerisms.
Provide concise observations for each speaker, avoiding summaries or paraphrasing of the conversation.
Your analysis should be based solely on the content and tone of the conversation, without external context.

For each line of the conversation, please provide an analysis in the following format:
'[Speaker_Y]: [sentiment_analysis_insight].'

Output:
Analyze the transcript for sentiments and psychological insights derived from the conversation. Provide insights about 
the speakers without summarizing or using keywords. Output should focus on sentimental analysis. Your responses should 
focus solely on the sentiment or psychological insights derived from the conversation. Avoid providing summaries, 
keywords, or any other extraneous information.

For example:
'[Speaker_1]: expresses a preference for physical activity, suggesting a proactive approach to health and well-being.'
'[Speaker_2]: demonstrates an interest in intellectual pursuits, indicating a preference for mental stimulation and learning.'

"""

prompt_v4 = """
Input:
Please provide a transcript of a conversation between two speakers.

Task: 
Extract sentiment and psychological insights from the conversation transcript provided by the hiring manager. 
Please refrain from providing a summary or keywords. Focus solely on identifying sentiments and psychological traits 
exhibited by the speakers.

Transcript:
{context}

Instructions:
Listen to the provided conversation transcript, ensuring it involves at least two speakers engaged in a natural conversation.
Extract insights regarding the sentiments expressed by each speaker, focusing on their emotional tone, attitude, and demeanor.
Identify any psychological traits or tendencies exhibited by the speakers based on their dialogue, tone of voice, and mannerisms.
Provide concise observations for each speaker, avoiding summaries or paraphrasing of the conversation.
Your analysis should be based solely on the content and tone of the conversation, without external context.

For each line of the conversation, please provide an analysis in the following format:
'[Speaker_Y] [sentiment_analysis_insight]'.

Output:
Analyze the transcript for sentiments and psychological insights derived from the conversation. Provide insights about 
the speakers without summarizing or using keywords. Output should focus on sentimental analysis. Your responses should 
focus solely on the sentiment or psychological insights derived from the conversation. Avoid providing summaries, 
keywords, or any other extraneous information.

For example:
'[Speaker_1] expresses a preference for physical activity, suggesting a proactive approach to health and well-being.'
'[Speaker_2] demonstrates an interest in intellectual pursuits, indicating a preference for mental stimulation and learning.'

Make sure you give the output in the below provided format:
{{
[Speaker_X]: [sentiment_analysis_insight]',
[Speaker_Y]: [sentiment_analysis_insight]'
}}

"""


def get_prompt(transcript: str) -> str:
    prompt = prompt_v3.format(context=transcript)
    return prompt

