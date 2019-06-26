from query_gen import QueryGenerator
from api_handling import SOHandler
from ranking import overall_confidence

query = input('Enter query: ')
qgen = QueryGenerator(query)
query_list = qgen.generate()

so = SOHandler()
answers = so.get_answers(query_list)
answers = sorted(answers, key = lambda x: overall_confidence(query, x),
                 reverse = True)

if len(answers) > 0:
    cnt = 0
    print('---------------------------- TOP 5 ANSWERS -------------------------------')
    for answer in answers:
        print('QUESTION:', answer.question_title)
        print('->\tAnswer by user:', answer.info['owner']['display_name'],'\n')
        answer.fetch_body()
        print(answer.to_markdown())
        print('Confidence: ', overall_confidence(query, answer))
        print('--------------------------------------------------------------------------')
        print()
        cnt += 1
        if cnt == 5: break;
else:
    print('Sorry, no answers found :(')
