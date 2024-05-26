system_message = """
You are an expert in various fields with a deep understanding of diverse subjects relevant to web-based research. Your expertise includes familiarity with the nuances of literature and information across multiple disciplines. When responding to users' inquiries, make sure to reference and incorporate relevant '## Source Information' effectively. Your answers should be precise, insightful, and cater to the specific interests and information needs of the users. Please maintain a professional and informative tone in your responses. Remember to respond in a language appropriate for the user's query, unless specifically requested otherwise.

Source Information
'''
{content}
'''

Additionally, the system should support extracting information from documents, like résumés, and automate the input of extracted data into specific formats, such as an Excel résumé template.

"""

user_message = """
氏名（フリガナ）：山上夏鈴　ヤマガミカリン
・生年月日：2000年07月17日（23歳）
・電話：080-2897-9687
・Mail：karin0717yamagamin@gmail.com

◆郵便番号：7200017
住所：広島県福山市千田町2-36-24-4

◆学歴
高校名：広島私立広島翔洋高等学校
入学年月：2016年4月
卒業年月：2019年3月

大学校名:福山平成大学福祉健康学部福祉学科
入学年月：2019年4月
卒業年月：2023年3月

◆取得資格　年月
2020年8月喀痰吸引第3号
2022年8月普通自動車第一種運転免許（AT限定）取得


◆職歴
社名：株式会社アールツーエス
入社：　　2023年　　　4月
退社：　2023　年　　　10月
ホームページ：https://r2s.co.jp/
雇用形態：正社員、一般事務
具体的な業務内容：
申請書の受付や日程調整、調査票の確認、行政への提出行っている。

社名:株式会社土屋
入社:2023年11月
退職:2023年2月
ホームページ:
雇用形態:非常勤、総務
具体的業務:
全社員の年末調整の書類作成、提出物の確認、ファイリング

◆自己PR
大学卒業後、一般事務と総務の仕事を経験いたしました。
仕事する上で大切にしていることは、2つあります。
一緒に仕事をしている人がより良い仕事をできるような環境作り、コミュケーションを積極的にとることを心かげております。調査票の確認などでは誤字脱字がないか相手が見て読みにくいものではないかを確認し、常に相手がいることを意識をして仕事に取り組んでおります。また、コミニュケーションを積極的に行うことで色んな方々の意見を取り入れることができ、私自身のスキルアップにも繋がり、そのスキルアップを生かして仕事に取り組むができ、効率よく仕事を進めていけると考えております。
貴社に入社いたしましたら、現状に満足するのではなく、日々新しいものをチャレンジをしていき、成長したいたと考えております。


◆配偶者　無
◆扶養義務　無
"""


