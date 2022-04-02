# Notify

A wrapper for `apprise`.

Add your apprise config `url` to `.env` file,

```text
# .env in the root directory or set the env variable,
APPRISE_URL=xxx-xxx-xxx-xxx
```

Usage,

```bash
from notify import notify

notify.notify("test message", title="this is title")
```
