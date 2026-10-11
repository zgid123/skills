FROM mcr.microsoft.com/devcontainers/javascript-node:1-22-bookworm

RUN corepack enable

RUN mkdir -p /home/node/.local/share/pnpm/store \
    && chown -R node:node /home/node/.local/share/pnpm
