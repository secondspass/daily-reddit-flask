#!/usr/bin/env python3
from app import app
import os


port = int(os.environ.get('PORT', 6312))
app.run(debug=True, use_reloader=True, port=port)
