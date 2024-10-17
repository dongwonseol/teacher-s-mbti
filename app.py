import streamlit as st
import random
import matplotlib.pyplot as plt
import numpy as np

# Streamlit app setup
st.set_page_config(page_title="교사 동물 유형 테스트 2.0", layout="centered")
st.title("🎓 교사 동물 유형 테스트 2.0 🎓")

# Questions data
questions = [
    {
        "question": "1. 학생들이 수업 시간에 떠들 때, 당신은 주로 어떻게 대처하나요?",
        "options": ["조용히 주의를 줍니다", "재미있는 농담으로 주의를 환기시킵니다"],
        "emoji": "👩‍🏫"
    },
    {
        "question": "2. 새로운 교육 방법을 도입할 때, 당신은 어떤 태도를 보이나요?",
        "options": ["기존의 검증된 방식을 선호합니다", "혁신적인 방법을 시도해보고 싶어합니다"],
        "emoji": "🔄"
    },
    {
        "question": "3. 학생의 과제가 늦게 제출되었을 때, 당신의 반응은?",
        "options": ["규칙은 규칙이다. 감점은 불가피합니다", "사정을 들어보고 융통성 있게 대처합니다"],
        "emoji": "📝"
    },
    {
        "question": "4. 수업 준비를 할 때, 당신의 스타일은?",
        "options": ["세세한 부분까지 꼼꼼히 계획합니다", "큰 틀만 잡고 즉흥적으로 진행합니다"],
        "emoji": "📚"
    },
    {
        "question": "5. 학생들과의 관계에서 당신이 중요하게 생각하는 것은?",
        "options": ["전문적이고 객관적인 관계 유지", "따뜻하고 친근한 관계 형성"],
        "emoji": "🤝"
    }
]

# State initialization
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
    st.session_state.answers = []

# Function to move to the next question
def next_question(answer):
    st.session_state.answers.append(answer)
    st.session_state.current_question += 1

# Display questions
if st.session_state.current_question < len(questions):
    question = questions[st.session_state.current_question]
    st.write(f"{question['emoji']} {question['question']}")
    
    for idx, option in enumerate(question['options']):
        if st.button(option):
            next_question('A' if idx == 0 else 'B')
else:
    # Display result after answering all questions
    st.subheader("결과")
    
    counts = {'A': st.session_state.answers.count('A'), 'B': st.session_state.answers.count('B')}
    primary_type = 'A' if counts['A'] > counts['B'] else 'B'
    secondary_type = random.choice(['A', 'B'])
    
    animal_types = {
        'AA': {'emoji': '🦉', 'name': "지혜로운 부엉이 선생님"},
        'AB': {'emoji': '🐘', 'name': "든든한 코끼리 선생님"},
        'BA': {'emoji': '🦒', 'name': "호기심 많은 기린 선생님"},
        'BB': {'emoji': '🐒', 'name': "활발한 원숭이 선생님"}
    }
    
    animal_type = animal_types[primary_type + secondary_type]
    st.write(f"{animal_type['emoji']} {animal_type['name']}")
    
    # Generate random chart data
    chart_data = np.random.uniform(60, 100, 5)
    
    # Plot radar chart
    labels = ['체계성', '유연성', '창의성', '친근성', '전문성']
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    angles += angles[:1]
    chart_data = np.concatenate((chart_data, [chart_data[0]]))
    
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, chart_data, color='blue', alpha=0.25)
    ax.plot(angles, chart_data, color='blue', linewidth=2)
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    
    st.pyplot(fig)

    st.write("공유 버튼을 누르면 결과를 친구들과 나눌 수 있습니다!")
    st.button("결과 재설정", on_click=lambda: st.session_state.clear())
