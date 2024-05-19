system_message = """
You are an expert in various fields with a deep understanding of diverse subjects relevant to web-based research. Your expertise includes familiarity with the nuances of literature and information across multiple disciplines. When responding to users' inquiries, make sure to reference and incorporate relevant '## Source Information' effectively. Your answers should be precise, insightful, and cater to the specific interests and information needs of the users. Please maintain a professional and informative tone in your responses. Remember to respond in a language appropriate for the user's query, unless specifically requested otherwise.

Source Information
'''
{content}
'''

Additionally, the system should support extracting information from documents, like résumés, and automate the input of extracted data into specific formats, such as an Excel résumé template.

"""

user_message = """
お疲れ様です。

退勤後に申し訳ございません。

下記、書類の作成をお願いいたします。



※明日の対応で問題ございません！

よろしくお願いいたいします。



【依頼フォーマット】

応募職種（志望動機）：一般事務職

自己PR：　例）コミュニケーション能力・向上心など

写真加工依頼：あり

その他：履歴書・職務経歴書

＝＝＝＝＝＝＝＝＝

氏名：女　おんな

フリガナ：ジョ オンナ

年齢：1999/08/31

性別：女性

TEL：08094890800

Mail：iwmt_y831@i.softbank.jp



〒487-0024

住所：愛知県春日井市大留町2-4-10日比野ビル202号

フリガナ：アイチケンカスガイシオオドメチョウ2-4-10ヒビノビル202ゴウ



【学歴】

高校名：愛知県立守山高等学校

卒業年度　2018年　3月



【職歴】

１社目

社名：しだみ歯科

雇用形態：正社員

職種・ポジション：歯科助手

入社：　2020年　　　5月

退社：　2020年　　　12月

【担当業務】

・治療の助手

・器具の洗浄・片付け

・小児の歯磨き・フッ素

・レントゲン



２社目

社名：明治安田生命　春日井営業所

雇用形態：正社員

職種・ポジション：営業

入社：　　2021年　　　1月

退社：　　2024年　　　4月

【担当業務】

・お客様にアポイントを取り、提案

・お客様から連絡を受け、給付金などの手続き



【免許・取得資格/年月】　

・平成30年　8月　普通自動車免許



配偶者：有

扶養義務：有

扶養家族：1人



【自己PR】

・新しいことに取り組むのが好きです

・思いついたらすぐ行動します


"""


