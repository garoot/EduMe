from django_elasticsearch_dsl import DocType, Index
from courses.models import Course

course = Index('courses')

course.settings(
    number_of_shards=1,
    number_of_replicas=0
)
@course.doc_type
class CourseDocument(DocType):
    class Meta:
        model = Course

        fields = [
            'course_name',
            'course_topic',
            'course_title',
            'course_description',
            'course_outcomes',
            'course_outline',
            'id',

        ]
