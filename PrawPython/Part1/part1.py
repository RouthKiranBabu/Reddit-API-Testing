import praw
import json

search = 'india'
post_limit = 5
comment_limit = 5

data = {
    "contents": []
}

reddit = praw.Reddit(client_id = 'G9heEJHCuVMWJTo64a-jng', 
                     client_secret = 'AO07lIvh5nSC5-vNsZFoSHxJ4kq_MQ',
                     username = 'ConsequenceShoddy488',
                     password = 'Reddit1!',
                     user_agent = 'ConsequenceShoddy488v1')

subreddit = reddit.subreddit(search)
hot_python = subreddit.top(limit=post_limit)
ids = 0
for submission in hot_python:
    data_ele = {}
    # print(dir(submission))
    # ['STR_FIELD', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_additional_fetch_params', '_chunk', '_comments_by_id', '_edit_experimental', '_fetch', '_fetch_data', '_fetch_info', '_fetched', '_kind', '_reddit', '_replace_richtext_links', '_reset_attributes', '_safely_add_arguments', '_url_parts', '_vote', 'add_fetch_param', 'all_awardings', 'allow_live_comments', 'approved_at_utc', 'approved_by', 'archived', 'author', 'author_flair_background_color', 'author_flair_css_class', 'author_flair_richtext', 'author_flair_template_id', 'author_flair_text', 'author_flair_text_color', 'author_flair_type', 'author_fullname', 'author_is_blocked', 'author_patreon_flair', 'author_premium', 'award', 'awarders', 'banned_at_utc', 'banned_by', 'can_gild', 'can_mod_post', 'category', 'clear_vote', 'clicked', 'comment_limit', 'comment_sort', 'comments', 'content_categories', 'contest_mode', 'created', 'created_utc', 'crosspost', 'delete', 'disable_inbox_replies', 'discussion_type', 'distinguished', 'domain', 'downs', 'downvote', 'duplicates', 'edit', 'edited', 'enable_inbox_replies', 'flair', 'fullname', 'gild', 'gilded', 'gildings', 'hidden', 'hide', 'hide_score', 'id', 'id_from_url', 'is_created_from_ads_ui', 'is_crosspostable', 'is_meta', 'is_original_content', 'is_reddit_media_domain', 'is_robot_indexable', 'is_self', 'is_video', 'likes', 'link_flair_background_color', 'link_flair_css_class', 'link_flair_richtext', 'link_flair_template_id', 'link_flair_text', 'link_flair_text_color', 'link_flair_type', 'locked', 'mark_visited', 'media', 'media_embed', 'media_only', 'mod', 'mod_note', 'mod_reason_by', 'mod_reason_title', 'mod_reports', 'name', 'no_follow', 'num_comments', 'num_crossposts', 'num_reports', 'over_18', 'parse', 'permalink', 'pinned', 'post_hint', 'preview', 'pwls', 'quarantine', 'removal_reason', 'removed_by', 'removed_by_category', 'reply', 'report', 'report_reasons', 'save', 'saved', 'score', 'secure_media', 'secure_media_embed', 'selftext', 'selftext_html', 'send_replies', 'shortlink', 'spoiler', 'stickied', 'subreddit', 'subreddit_id', 'subreddit_name_prefixed', 'subreddit_subscribers', 'subreddit_type', 'suggested_sort', 'thumbnail', 'thumbnail_height', 'thumbnail_width', 'title', 'top_awarded_type', 'total_awards_received', 'treatment_tags', 'unhide', 'unsave', 'ups', 'upvote', 'upvote_ratio', 'url', 'url_overridden_by_dest', 'user_reports', 'view_count', 'visited', 'wls']
    if not submission.stickied:
        print("\nSubmission not stickied\nTitle: {}\nUps: {}, Down: {}.\nVisited: {}.".format(
        submission.title,
        submission.ups, 
        submission.downs, 
        submission.visited))
        data_ele["id"] = ids; ids += 1
        data_ele["Title"] = submission.title
        data_ele["Ups"] = submission.ups
        data_ele["Downs"] = submission.downs
        data_ele["Visited"] = submission.visited
        data_ele["Comments"] = []
        i = 0
        comments = []
        submission.comments.replace_more(limit = 0)
        for comment in submission.comments.list():
            if i >= comment_limit: break
            print("\nParent id: " + str(comment.parent()))
            print("Comment id: " + str(comment.id))
            try:
                print(comment.body)
                comments.append(comment.body)
                data_ele["Comments"].append(comment.body)
            except Exception as e:
                print(e)
            i += 1  
         
    else:
        print("\nSubmission stickied\nTitle: {}\nUps: {}, Down: {}.\nVisited: {}.".format(
        submission.title,
        submission.ups, 
        submission.downs, 
        submission.visited))
    data["contents"].append(data_ele)

# print(data)

# Step 2: Specify the filename
filename = "data.json"

# Step 3: Write the data to a JSON file
with open(filename, 'w') as json_file:
    json.dump(data, json_file, indent=4)  # Use indent=4 for pretty formatting

print(f"JSON file '{filename}' created successfully!")
