from contextvars import ContextVar, copy_context
from contextlib import contextmanager
from typing import overload


class Context[T]:
    context: ContextVar[T]

    @overload
    def __init__(self, name: str, default: T = ...):
        ...  # pragma: nocover

    @overload
    def __init__(self, name: str):
        ...  # pragma: nocover

    def __init__(self, name: str, default: T | None = None):
        if default:
            self.context = ContextVar(name, default=default)
        else:
            self.context = ContextVar(name)

    @contextmanager
    def provide(self, value: T):
        def _inner():
            token = self.context.set(value)
            yield self.context
            self.context.reset(token)

        return copy_context().run(_inner)

    def get(self):
        try:
            return self.context.get()
        except LookupError as e:
            raise LookupError(
                "Cannot get value of given context, perhaps you forgot to call .provide() or wrap it inside with statement?"
            ) from e


def use_context[T](context: Context[T]) -> T:
    return context.get()
