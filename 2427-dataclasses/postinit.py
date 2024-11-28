from dataclasses import InitVar, dataclass, field


@dataclass()
class Responder:
    cache_ttl: int = field(default=300, repr=False)
    disable_cache: InitVar[bool] = False

    def __post_init__(self, disable_cache: bool) -> None:
        if disable_cache:
            self.cache_ttl = 0

    @property
    def cache_disabled(self) -> bool:
        return self.cache_ttl == 0


r = Responder(disable_cache=True)
print(r.cache_ttl)
print(r.cache_disabled)
