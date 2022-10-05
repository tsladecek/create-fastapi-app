#!/bin/sh
# Create symbolic links to hooks specified in git hooks directory
for filename_raw in git_hooks/*; do
  filename=$(echo "$filename_raw" | cut -d "/" -f 2)
  filename_base=$(echo "$filename" | cut -d "." -f 1)

  chmod +x "$filename_raw"
  ln -s ../../git_hooks/"$filename" .git/hooks/"$filename_base"
done
