from survey import AnonymouseSurvey

# 定义一个问题，并创建一个表示调查的 AnonymousSurvey 对象
question = "What language did you first learn to spead?"
language_survey = AnonymouseSurvey(question)

# 显式问题并存储答案
language_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == "q":
        break
    language_survey.store_response(response)

# 显式调查结果
print("\nThank you to everyone who participated in the survey!")
language_survey.show_results()
