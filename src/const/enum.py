import enum


class POST_STATUS(enum.Enum):
    DRAFT = "Draft"
    PUBLISHED = "Published"
    PENDING = "Pending"

class PRODUCT_STATUS(enum.Enum):
    DRAFT = "Draft"
    PEDDING = "Pending"
    PUBLISHED = "Published"