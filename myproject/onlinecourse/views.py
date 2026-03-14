from django.shortcuts import render
from .models import Course, Submission

def submit(request, course_id):
    score = 5
    Submission.objects.create(
        user=request.user,
        course_id=course_id,
        score=score
    )
    return render(request, "onlinecourse/result.html", {"score": score})


def show_exam_result(request, submission_id):
    submission = Submission.objects.get(id=submission_id)
    return render(
        request,
        "onlinecourse/result.html",
        {"score": submission.score}
    )