import time
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Note(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    
    def dict(self, *args, **kwargs):
        # 调用父类的dict方法获取基本字典
        data = super().dict(*args, **kwargs)
        # 将datetime字段转换为字符串
        data['created_at'] = data['created_at'].isoformat()
        return data
