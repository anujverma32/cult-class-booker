class ReprMixin:
    def __repr__(self):
        try:
            fields = ", ".join(
                f"{col.name}={getattr(self, col.name)!r}"
                for col in self.__table__.columns
            )
            return f"<{self.__class__.__name__} {fields}>"
        except Exception as e:
            return f"<{self.__class__.__name__} (error: {e})>"
