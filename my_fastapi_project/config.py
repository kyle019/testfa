from pydantic import BaseModel

class ServerConfig(BaseModel):
    protocol: str
    rest_api_host: str
    rest_api_port: int
    python_django_host: str
    python_django_port: int
    run_path: str
    log_path: str
    debug: bool

class PathConfig(BaseModel):
    example: str
    server_status: str
    server_cpu: str
    server_memory: str
    application_transaction: str
    application_cpu: str
    application_memory: str
    application_heap: str
    gc: str
    heap_percent: str
    heap_used: str
    topology_inbound: str
    topology_db: str
    topology_system: str
    was: str
    transaction_detail: str
    transaction_error_filter: str
    transaction_error_http: str
    transaction_error_program: str
    transaction_error_sql: str
    transaction_section: str
    transaction_drill: str
    connection_pool: str
    sql_query_latency: str
    sql_query_count: str
    sql_query_error_count: str
    threshold: str
    threshold_analysis: str
    threshold_alarm: str
    performance_monitor: str

class APIConfig(BaseModel):
    tags_metadata: list

server_config = ServerConfig(
    protocol="http",
    rest_api_host="192.168.251.238",
    rest_api_port=8000,
    python_django_host="192.168.221.34",
    python_django_port=8000,
    run_path="run",
    log_path="logs",
    debug=True
)

path_config = PathConfig(
    example="f0/example",
    server_status="f1/status",
    server_cpu="f1/cpu",
    server_memory="f1/memory",
    application_transaction="f1/application",
    application_cpu="f2/cpu",
    application_memory="f2/memory",
    application_heap="f2/heap",
    gc="f3/garbage_collection",
    heap_percent="f4/memory_alarm_percent",
    heap_used="f4/memory_alarm_used",
    topology_inbound="f5/inbound",
    topology_db="f5/db",
    topology_system="f5/system",
    was="f6/was",
    transaction_detail="f7/transaction_detail",
    transaction_error_filter="f7/transaction_error_filter",
    transaction_error_http="f7/transaction_error_http",
    transaction_error_program="f7/transaction_error_program",
    transaction_error_sql="f7/transaction_error_sql",
    transaction_section="f8/transaction_section",
    transaction_drill="f9/transaction_drill",
    connection_pool="f11",
    sql_query_latency="f12/sql_query_latency",
    sql_query_count="f12/sql_query_count",
    sql_query_error_count="f12/sql_query_error_count",
    threshold="f13",
    threshold_analysis="f14",
    threshold_alarm="f15",
    performance_monitor="performance/monitor"
)

api_config = APIConfig(
    tags_metadata=[
        {"name": "F0", "description": "bmt 호출 테스트"},
        {"name": "F1", "description": "실시간 대시보드 제공 기능"},
        {"name": "F2", "description": "어플리케이션 모니터링 기능"},
        {"name": "F4", "description": "메모리 누수 감지 및 분석 기능"},
        {"name": "F5", "description": "토폴로지 뷰 기능"},
        {"name": "F6", "description": "이기종 WAS의 실시간 통합 모니터링 기능"},
        {"name": "F7", "description": "트랜젝션 응답시간 분포도 제공 기능"},
        {"name": "F8", "description": "구간별 응답시간 제공 기능"},
        {"name": "F9", "description": "응답저하 트랜젝션 대한 상세 분석(Drill-Down) 기능"},
        {"name": "F11", "description": "Connection Pool 모니터링 기능"},
        {"name": "F12", "description": "SQL 상세 모니터링 기능"},
        {"name": "F13", "description": "임계값 설정 및 알람 기능"},
        {"name": "F14", "description": "임계값 초과 항목에 대한 메서드 레벨의 원인 분석 기능"},
        {"name": "F15", "description": "장애 발생 시 담당자 통보 기능"},
        {"name": "F16", "description": "관리자에 의한 임계값 초과 쓰레드 허용 차단 설정 기능"},
        {"name": "F17", "description": "쓰레드 강제 종료 기능"},
    ]
)
