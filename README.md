# logbook
Inspired by *Steal Like an Artist*, a logbook app to record your victories.

![screenshot](img/lb_ss_50pct.png)

## Warning!
If you put this on your website, you should absolutely learn how [htaccess](https://www.seas.upenn.edu/cets/answers/auth-htpasswd.html) works and use it in the upload/ directory.  Otherwise, who knows what people might put into your log?  Another option is to put it in the root logbook directory, to keep the whole thing private.

## TODO
* On upload, use ImageMagick to create a smaller version to reduce load times.  Link to original version in main view.
* Only load so many at a time
* Add search
