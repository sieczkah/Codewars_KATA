"""https://www.codewars.com/kata/5b16490986b6d336c900007d"""

def my_languages(results):
    results_list = sorted(results.items(), key=lambda x: x[1], reverse=True)
    return [lang for lang, score in results_list if score >=60]
