

def test_touch_updates_timestamp(self):
    from models.base import BaseModel
    b = BaseModel()
    old = b.updated_at
    b.touch()
    self.assertGreaterEqual(b.updated_at, old)

def test_to_dict_has_iso_dates(self):
    from models.base import BaseModel
    b = BaseModel()
    data = b.to_dict()
    # klucze są
    self.assertIn("id", data)
    self.assertIn("created_at", data)
    self.assertIn("updated_at", data)
    # format ISO (z literą 'T')
    self.assertIn("T", data["created_at"])
    self.assertIn("T", data["updated_at"])
