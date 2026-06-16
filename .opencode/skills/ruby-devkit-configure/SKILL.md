---
name: ruby-devkit-configure
description: Configure Ruby + MSYS2 toolchain on Windows. Use when native gems fail or switching versions.
---

# Ruby DevKit Configuration

Use this skill when:
- Native gem installation fails (bigdecimal, http_parser.rb)
- Switching between Ruby 3.1/3.2 on Windows

## Install Ruby with DevKit

winget install --id RubyInstallerTeam.RubyWithDevKit.3.1 -e

## Enable MSYS2

rtk ridk enable

## Configure Bundler

bundle config set path vendor/bundle
bundle install

## Fix Gemfile.lock for Linux CI

bundle lock --add-platform x86_64-linux
