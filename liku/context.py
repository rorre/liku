from contextvars import ContextVar, copy_context
from contextlib import contextmanager
from typing import Callable, overload

from liku.elements import HTMLNode


class Context[T]:
    """Primitive context type to share state between components."""

    context: ContextVar[T]

    @overload
    def __init__(self, name: str, default: T = ...): ...  # pragma: nocover

    @overload
    def __init__(self, name: str): ...  # pragma: nocover

    def __init__(self, name: str, default: T | None = None):
        if default:
            self.context = ContextVar(name, default=default)
        else:
            self.context = ContextVar(name)

    @contextmanager
    def provide(self, value: T):
        """Context manager to provide value to all consumer of this context. Thread safe.

        Args:
            value (T): Value to assign.
        """

        def _inner():
            token = self.context.set(value)
            yield self.context
            self.context.reset(token)

        return copy_context().run(_inner)

    def get(self):
        """Gets current value of this context

        Raises:
            LookupError: If value has never been set via .provide() and no default is set.

        Returns:
            T: Value of this context
        """
        try:
            return self.context.get()
        except LookupError as e:
            raise LookupError(
                "Cannot get value of given context, perhaps you forgot to call .provide() or wrap it inside with statement?"
            ) from e

    def Provider(self, value: T, children: Callable[[], HTMLNode]):
        with self.provide(value):
            return children()


def use_context[T](context: Context[T]) -> T:
    """Fetches current value of given context.

    Returns:
        T: Current value of the context
    """
    return context.get()
