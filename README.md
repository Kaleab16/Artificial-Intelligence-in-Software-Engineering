# AI Preemptive Bug Fixing

## Objective
Fix logical and memory safety issues in a linked list insertion function using AI-assisted debugging.

## Files
- initial_code.c (buggy version)
- refactored_code.c (fixed version)

## Issues Found

### Logical Error
Traversal reached NULL, so assignment did not link node properly.

### Memory Safety Issue
Missing malloc NULL check → potential segmentation fault.

## Fix Summary
- Correct pointer traversal
- Proper node linking
- Added malloc safety check
