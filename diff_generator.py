
import diff_match_patch as dmp_module

dmp = dmp_module.diff_match_patch()

def generate_diff(original_text, modified_text):
    diffs = dmp.diff_main(original_text, modified_text)
    dmp.diff_cleanupSemantic(diffs)
    return diffs

def diff_to_json(diffs):
    return [{"operation": op, "text": text} for op, text in diffs]
