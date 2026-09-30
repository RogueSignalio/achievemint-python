# achievemint/errors.py

class AchievemintError(Exception):
    """Base exception for all achievemint client errors."""
    pass


class AuthenticationError(AchievemintError):
    """Raised when authentication with the API fails."""
    pass


class NotFoundError(AchievemintError):
    """Raised when a requested resource doesn't exist."""
    pass


class ClientError(AchievemintError):
    """Raised for client API responses."""
    pass

class ApiError(AchievemintError):
    """Raised for other unexpected API responses."""
    pass
