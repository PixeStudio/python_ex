from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
import uuid

def utcnow():
    """Always timezone-aware UTC now"""
    return datetime.now(timezone.utc)

@dataclass
class BaseModel:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    created_at: datetime = field(default_factory=utcnow)
    updated_at: datetime = field(default_factory=utcnow)

def touch(self) -> None:
    """Update the 'updated_at timestamp'"""
    self.updated_at = utcnow()

def to_dict(self) -> dict:
    """Serialize to JSON friendly dict (ISO timestamps)"""
    d = asdict(self)
    d["created_at"] = self.created_at.isoformat()
    d["updated_at"] = self.updated_at.isoformat()
    return d
