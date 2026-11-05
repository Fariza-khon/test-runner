```mermaid
erDiagram
    TEST_RUN ||--o{ TEST_CASE_RESULT : contains

    TEST_RUN {
        int id PK
        string project_path
        string status
    }
    TEST_CASE_RESULT {
        int id PK
        int run_id FK
        string test_name
        string status
    }