**[알고리즘] 영역**

**1-1**번 문제

 

![img](file:////Users/jypsnewmac/Library/Group%20Containers/UBF8T346G9.Office/msoclip1/01/clip_image002.gif)

설명: 함수 number_classifying 를 정의하고 n1, n2를 인자로 받도록 했습니다. 딕셔너리에 들어갈 키를 홀수 및 짝수로 정의했습니다. n1>n2일 때 evens에는 n을 2로 나누었을 때 0으로 떨어지는 값을 넣도록 했고, odds에는 n을 2로 나누었을 때 0으로 떨어지지 않는 값을 넣었습니다. 범위는 n2에서 n1까지입니다. n1<n2일 때도 마찬가지로 적용했습니다.

이후 딕셔너리 number_list를 정의하고 temp_keys에서 Key의 이름을 가져오도록 했습니다. 딕셔너리의 even_number 키에는 evens를 리스트 형식으로 넣고, odd_number 키에는 odds를 리스트 형식으로 넣습니다. 이후 number_list를 출력합니다.

 

 

 

 

**1-2번 문제**

 

![img](file:////Users/jypsnewmac/Library/Group%20Containers/UBF8T346G9.Office/msoclip1/01/clip_image004.gif)

설명: 빈 리스트 num_list와 함수 creator를 정의합니다. 임의의 값 up를 1로 지정해두고, 함수 creator에서 입력받는 num의 값과 비교합니다. 만약 up이 num보다 작다면, temp라는 변수를 선언하여 up과 up의 각 자리 숫자를 더한 값을 지정합니다. 만약 temp의 값이 num과 같다면 빈 리스트 num_list에 up을 추가합니다. temp의 값과 num이 동일한 지의 유무와 관련 없이, up이 num보다 작을 때까지 while 반복문 안에서 up에 계속 1을 더합니다. 반복하면서 up이 num과 같아지는 상황이 올 경우 while문을 종료합니다. 이후 num_list를 최종적으로 출력합니다.

 

 

 

 

 

**[****데이터** **분석****]** **영역**

 

\1.     GH회사에서는 이번 9월 신제품 광고 캠페인을 유튜브에서 집행하고자 합니다. 우선 GH사는 수집한 데이터의 관계를 이해하기 위해 **1)** **좋아요** **수와** **싫어요** **수의** **관계****, 2)** **싫어요** **수가** **댓글의** **수에** **미치는** **영향**을 분석하고자 합니다. 1번 분석은 단순 플로팅(plotting)으로, 2번 분석은 단순선형회귀모델로 표현하여 독립 변수가 종속 변수에 어떻게 유의미한 영향을 미치는지 간단하게 설명해주세요. **시각** **자료** **및** **코드를** **제외한** **답안의** **길이는** **한** **페이지** **이내로** **제한해주세요****.**

 

**1-1.** **좋아요** **수와** **싫어요** **수의** **관계**

 

파이썬 코드 (GHdata_Q11.py) 

![https://lh3.googleusercontent.com/3tVTb2SqJmbQ2JtaE9Z3snVmE41OaiZYcjZDhzFemonIvocxzcsZ8iHRKyZgctNI-luG8qUQOLV_rxxKVSJDJe7TDqz07ANGTkFKjXZdXfNvyUG8oYUZksQSOKso4kWtQ53IRQCq](file:////Users/jypsnewmac/Library/Group%20Containers/UBF8T346G9.Office/msoclip1/01/clip_image006.gif)

Plotting 시각 자료

![https://lh5.googleusercontent.com/GcLxB27ZgysMXuDWQFhSUVYTn_NSfZe6aB1vXiFoR2_BnY_RMFs-BRy66JAj4VdPAtuBvD7T7wxJlZ-0bScf6sfu4o8WgDsXjfTs3QsvX_TQ4LTbbTSSzC_jLIzh-6rq2Zkx-0wC](file:////Users/jypsnewmac/Library/Group%20Containers/UBF8T346G9.Office/msoclip1/01/clip_image008.gif)

설명: 좋아요(avgLike)의 수가 증가할 수록 싫어요(avgDislike) 수도 비례하게 증가하는 것으로 나타났다. 이러한 현상은 좋아요 0개에서 약 7천 개 사이에서 분명한 흐름이 관찰된다. 단, 좋아요 1만 개 이상의 경우 데이터가 부족하여 상관관계를 확정하기 어렵다.

**1-2.** **싫어요** **수가** **댓글의** **수에** **미치는** **영향**

 

파이썬 코드(GHdata_Q12.py)

![https://lh3.googleusercontent.com/fxG8NdQZgFmM6KnSKHt1r6jPYS2bo34Ja_PGz82LzrShKGADe3yorA4z4_JxhbeZT40VctNHH9uNKXNULd6hderWKWW6ctweR-R49HqZKuMHG6FE4KLPHJfkCdXZ_afr9pHXqnP5](file:////Users/jypsnewmac/Library/Group%20Containers/UBF8T346G9.Office/msoclip1/01/clip_image010.gif)

 

결과 화면

![https://lh4.googleusercontent.com/XWY7TdzmK4Z_kVGUWdYAY72DPJ-_AFXjaypH3JKRluRcv0AHoYFH3SOzl6sdS9YYbaIiQjCxL80O6e2RUOr9cQAKDFRUK6uReci4sqW5NP3MXuUPi-XWeEJJ4ubFsRpFJaA_yCqE](file:////Users/jypsnewmac/Library/Group%20Containers/UBF8T346G9.Office/msoclip1/01/clip_image012.gif)

 

설명: 싫어요 수가 증가할 수록 댓글의 수도 증가하는 것으로 나타났다. 위의 보고서 해석은 다음과 같다.

 

\1.     R 제곱 값(R-squared): 0.555이므로 해당 데이터프레임을 설명하는 모델이 avgComment 변동성의 55.5%를 설명하는 것으로 해석된다. 0.4를 넘으므로 유의미한 모델이라고 평가할 수 있다.

\2.     Co-efficient(계수): intercept이 157이고 avgDislike가 3.3520이다. 모델식으로 표현하면 avgComment = 3.3520 x avgDislike + 157.4636 이라고 설명할 수 있다.

\3.     P>|t|(유의확률): 일반적으로 독립변수가 95%의 신뢰도를 가져야 유의미하다고 판단되므로, 독립변수의 유의확률은 0.05보다 작은 값이 나와야 한다. avgDislike의 유의확률은 0이므로, 독립변수가 종속변수에 미치는 영향이 유의미하다고 설명할 수 있다.

\4.     Durbin-Watson(더빈왓슨, DW검정): DW검정 값이 1.8666이다. 일반적으로 1.5~2.5 사이가 나오면 독립으로 판단하므로 회귀모형이 적합하다는 것을 의미한다.

\2. GH사는 신제품 홍보를 목적으로 가능한 적은 비용으로 가장 많은 광고 도달을 유도하기 위해 유튜버를 광고모델로 선정하고자 합니다. 다양한 접근 방식으로 변수들 간의 관계를 이해해보고, GH사에게 적합한 유튜버 3명을 근거와 함께 제안해주세요. 유튜버를 고용하는 비용은 유튜버의 구독자 수(subscriberCount)에 비례함을 가정합니다. 제안하는 과정에 필요한 추가적인 가정은 자유롭게 설정하되 명시해주세요. **시각** **자료** **및** **코드를** **제외한** **답안의** **길이는** **한** **페이지** **이내로** **제한해주세요****.**

파이썬 코드(GHdata_Q2.py)

![https://lh3.googleusercontent.com/k5tohMc_mk38THKixzNpBk7WNcnITn0tijetYL0JDhv10Fa309uScoUkwJ_QqeFvwGc4wqZW9Cw5N3Lkq0mbB6VmvBWwFgQY_1ljPQwKaUgrpkhw46tHeL5ahWnDWKuCaxHnRacK](file:////Users/jypsnewmac/Library/Group%20Containers/UBF8T346G9.Office/msoclip1/01/clip_image014.gif)

**결과** **화면**

![https://lh5.googleusercontent.com/Lok2Odd9WDDpqe9ytXNoNt3mTXiY0NFXjz8KwIINuw34Gj8UtuaET5U6LypL5QykhA_lKLMCqJ6ktE1Z_iNWEVnpuXaBorOpPoKOT1YE-If91yr7LnCwBElDk02srYVcLJkdGG0f](file:////Users/jypsnewmac/Library/Group%20Containers/UBF8T346G9.Office/msoclip1/01/clip_image016.gif)

**답안**: JS, Frederick, Oscar

**설명**

가능한 가장 적은 비용으로, 가장 많은 광고 도달을 유도하기 위해서 다음의 수식을 도출했습니다.

![https://lh5.googleusercontent.com/EUsGfxjEVrl6nO6Q4vzQ6a5NE3DhtyCpGA0RwiRB38bU1OHCX48FjrY_0rdshflO8BTL1IELbSQqAc9eLyhYdWmWi_2q8Fi6ufcH3yapB4fkOzY4DsBbNmm5DujqCY9J65GmhfAy](file:////Users/jypsnewmac/Library/Group%20Containers/UBF8T346G9.Office/msoclip1/01/clip_image018.gif)

주어진 데이터에 비디오 별 평균 시청 횟수가 나오지 않았음으로, 유사한 데이터를 얻기 위하여 realLike라는 변수를 설정했습니다. 좋아요를 누르는 것은 시청자가 영상에 반응하는 가장 쉬운 방법입니다. 높은 신빙성을 지닌 자료를 발견하지는 못했으나, 여러 마케팅 에이전시의 사이트에서 좋아요 수와 시청 횟수는 유의미한 양의 상관관계를 갖는다는 정보가 있습니다.([링크 1](https://tubularinsights.com/3-metrics-youtube-success/), [링크 2](https://philosophiren.com/311?category=745293)) 또한, 비용의 효율성을 따지기 위하여 평균 좋아요 수(avgLike)를 전체 구독자 수(subscribersCount)로 나누어 realLike라고 정의했습니다. realLike가 높을 수록 적은 비용으로 많은 시청 수(또는 영상에 대한 관심도)를 보인다고 말할 수 있습니다.

 

![https://lh4.googleusercontent.com/f7WQEEIWq3oTsoK5nljUOYLafGyie129-RGbidZyP8a2FiKqboZkUel0pQa5lcSgZxw5qQz-PdSuY8G57npSOMUJLbkIM-8PkrOAOGT6QZwIHjeeznT8CLx7xJg3Eq7Mr-84M44k](file:////Users/jypsnewmac/Library/Group%20Containers/UBF8T346G9.Office/msoclip1/01/clip_image020.gif)

realDisLike도 realLike와 동일한 논리를 차용하여 수식을 도출했습니다. 전체 구독자 수에 대비해 동영상 한 개에 남겨지는 부정적인 반응(싫어요)를 정의했습니다.

![https://lh3.googleusercontent.com/8DSEWMHDaRmNzcCOVKWPl-4UIhNE_EO2lv9vsC0MfFyXJyk4KkoHq-oj0z0zmw6Lpo3lLHapEEo2fljMGKv4q29tb1qVfyYPB_IBqHaat0p-TCp3yPSBraqMWQW0W08OEUod02vn](file:////Users/jypsnewmac/Library/Group%20Containers/UBF8T346G9.Office/msoclip1/01/clip_image022.gif)

평가의 기준으로서 realDisLike를 realLike로 나눈 metrics라는 변수를 정의했습니다. 비용 효율성을 고려한 실제 긍정 반응 대비 부정 반응을 확인하고자 하였습니다. metrics의 값이 낮은 것이 좋은 옵션이라고 할 수 있는데, 그 이유는 한 개의 ‘좋아요’ 당 달리는 ‘싫어요’ 의 비율이 떨어지기 때문입니다. 따라서 높은 조회수를 가져가면서 시청자의 긍정적인 반응을 얻는 유튜버로 생각할 수 있습니다.

기타 변수들 간의 관계는 다음의 경우를 상정했습니다.

·       recentFrequency: 구체적인 논문 결과를 찾지 못했으나, 일 주일에 최대한 많은 수의 영상을 꾸준히 올리는 것이 [유튜브 알고리즘 상에서 최상단 검색결과를 얻을 수 있는 방법](https://medium.com/@joshdance/decoding-the-youtube-algorithm-for-fun-and-profit-5dba0de8561a)이라는 글이 있습니다. 따라서 현실적으로 일 주일에 2회 이상 꾸준히 동영상을 업로드하는 유튜버를 선정 대상으로 고려했습니다.

·       idconcentration: 해당 비율이 높을 수록 많은 사람들이 댓글을 단다는 것을 의미합니다. 최소한 해당 비율이 0.5 이상인 유튜버를 선정 대상으로 고려했습니다.