# Declarative Memory Profiling

[![awesome plugin](https://custom-icon-badges.demolab.com/static/v1?label=&message=awesome+plugin&color=383938&style=for-the-badge&logo=cheshire_cat_ai)](https://)

![alt text](declarative_memory_profiling_logo.png)

Loosely inspired by Quivr's "[brain](https://docs.quivr.app/getting-started/brain)" concept. The plugin allows you to profile loading and retrieval into and from declarative memory using a profile set in the working memory

## Usage


1. Install and activate the plugin
2. Activate a profile for the session with the `command`:
```python
@p profile_name
```
![alt text](screenshots/1_change_profile_and_upload_doc.png)
> Two manuals with two different profiles have been uploaded


4. Load documents into the selected profile and query the profiled memory

![alt text](screenshots/2_same_question_profile_1.png)
![alt text](screenshots/2_same_question_profile_2.png)
> for the same question we receive the response profiled according to the selected profile


## Todo

 - [ ] Remove profile management commands from history
 - [ ] Create two more layers regarding memory profiling (public/global, private/user)
 - [ ] Allow profile forcing/selection via additional parameter in user message

> **Important**
> A new release of your plugin is triggered every time you set a new `version` in the `plugin.json` file.
> Please, remember to set it correctly every time you want to release an update.

