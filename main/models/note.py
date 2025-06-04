import time
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Note(BaseModel):
    id: Optional[int] = 0
    title: Optional[str] = None
    content: Optional[str] = None
    created_at: Optional[datetime] = None
    
    def dict(self, *args, **kwargs):
        # 调用父类的dict方法获取基本字典
        data = super().dict(*args, **kwargs)
        # 将datetime字段转换为字符串
        if data['created_at'] is not None:
            data['created_at'] = data['created_at'].isoformat()
        return data
