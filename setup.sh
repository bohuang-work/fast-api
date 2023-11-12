#!/bin/bash

set -e

# Install dev dependencies
task install:helm
task install:k3d
# task install:k9s
task install:kubectl