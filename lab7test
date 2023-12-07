import pytest
from mytask7 import shake_ball, add_response

responses = {
    "answer": ["Так", "Ні", "Можливо"],
    "probability": [1/3, 1/3, 1/3],
}

# Перевірка чи тип поверненого результату є стрічкою
def test_type_result_func():
    assert isinstance(shake_ball(responses), str)

@pytest.mark.parametrize('new_response,probability', [
    ('New Answer', 0.2),
    ('Another Answer', 0.3),
    ('Yet Another Answer', 0.5),
])
def test_add_response(new_response, probability):
    add_response(responses, new_response, probability)
    assert new_response in responses["answer"]
    assert probability in responses["probability"]

@pytest.mark.parametrize('question', [
    'Is it raining today?',
    'How are you?',
    'What is the capital of France?',
])
def test_shake_ball(question):
    answer = shake_ball(responses)
    assert answer in responses["answer"]
