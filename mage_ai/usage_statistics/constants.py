import enum

API_ENDPOINT = 'https://api.mage.ai/v1/usage_statistics'


class EventNameType(str, enum.Enum):
    BLOCK_RUN_ENDED = 'block_run_ended'
    USAGE_STATISTIC_CREATE = 'usage_statistic.create'
    PIPELINE_RUN_ENDED = 'pipeline_run_ended'


class EventActionType(str, enum.Enum):
    CREATE = 'create'
    DENY = 'deny'
    EXECUTE = 'execute'
    IMPRESSION = 'impression'


class EventObjectType(str, enum.Enum):
    BLOCK = 'block'
    BLOCK_RUN = 'block_run'
    CHART = 'chart'
    CUSTOM_TEMPLATE = 'custom_template'
    ERROR = 'error'
    FEATURE = 'feature'
    PIPELINE = 'pipeline'
    PIPELINE_RUN = 'pipeline_run'
    PROJECT = 'project'
    USER = 'user'
