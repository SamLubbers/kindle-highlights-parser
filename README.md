# Kindle highlights parser

Simple script to transform kindle csv export to text file.

Currently (30/4/2021) kindle exports your notes in a csv file, with each row
containing a certain highlight or note at a given location in the book. This is
not the most appropriate output format if you want to store or review your
notes. This script converts the data in the csv to a text format, in which notes
are separated by chapter.

# How to use this script

1. Download the notes from your kindle to your computer. 
  - In your kindle, open a book and go to `GO TO > Notes > Export Notes`
  - Download the `.csv` file with the notes sent to your email
2. Download the file `parse_kindle_highlights.vim` from this repository. 
3. Open a terminal and run this command

```bash
vim <path_to_notes> -S <path_to_script>
```

- `<path_to_notes>` is the path to the place in your computer where you've stored
the notes from step 1
- `<path_to_script>` is the path to the place in your computer where you've stored
the script you've downloaded in step 2

For example, your script might be:

```bash
vim ~/Downloads/Che Guevara Reader_ Writings on Politics & Revolution-Notebook.csv -S ~/scripts/parse_kindle_highlights.vim
```

4. Rename the resulting file `kindle_highlights.md` and move it to your desired
   directory

