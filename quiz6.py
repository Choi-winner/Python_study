# 파일을 만드는 매크로.
# 50개의 보고서를 각각 작성해서 파일로 저장하는 프로그램을 작성하시오.

for i in range(1,51):
    with open('{0}주차.txt'.format(i), 'w', encoding='utf8') as report:
        report.write('''- {0} 주차 주간보고 -
부서 :
이름 :
업무 요약 :'''.format(i))

