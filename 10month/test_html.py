# Dash 프레임워크에서 필요한 컴포넌트 가져오기
from dash import Dash, dcc, html, Input, Output
# Plotly의 그래프 객체 모듈(go): Figure, Bar 등 그래프 생성에 사용
import plotly.graph_objects as go

# Dash 앱 인스턴스 생성. __name__은 정적파일 경로 등 내부 설정에 쓰임
app = Dash(__name__)

# 앱이 그릴 웹 페이지의 레이아웃 정의
app.layout = html.Div([
    # 제목 헤더
    html.H4('Interactive color selection with simple Dash example'),
    # 안내 문구
    html.P("Select color:"),
    # 드롭다운 위젯. 사용자가 색상을 고르면 value가 바뀜
    dcc.Dropdown(
        id="dropdown",                              # 콤포넌트 식별자
        options=['Gold', 'MediumTurquoise', 'LightGreen'],  # 표시/선택 가능한 값 목록
        value='Gold',                               # 초기 선택값
        clearable=False,                            # X 버튼으로 비우기 금지
    ),
    # 그래프 표시 영역. 콜백에서 figure 속성을 채워 넣음
    dcc.Graph(id="graph"),
])

# 콜백: 입력과 출력을 선언적으로 연결


@app.callback(
    Output("graph", "figure"),   # graph 컴포넌트의 figure 속성에 출력
    Input("dropdown", "value"))  # dropdown의 현재 선택값을 입력으로 받음
def display_color(color):
    # 선택된 color를 막대 색으로 사용하는 Figure 생성
    fig = go.Figure(
        data=go.Bar(
            y=[2, 3, 1],          # 예시 데이터. 원하는 데이터로 교체 가능
            marker_color=color    # 막대 색상을 드롭다운 선택값으로 설정
        )
    )
    return fig                   # 생성한 Figure를 반환하면 화면이 업데이트됨


# 개발 서버 실행. debug=True면 코드 변경 시 자동 리로드 및 에러 페이지 제공
app.run(debug=True)
# 참고: app.run_server(debug=True) 형태도 동일하게 사용 가능
