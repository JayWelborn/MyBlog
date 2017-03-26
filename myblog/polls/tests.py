# Standard library imports
from datetime import timedelta

# Django imports
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

# Relative imports
from .models import Question, Choice


def create_question(question_text, days):
    """
    Creates a question with the given 'question_text' and published
    given number of 'days' offset to now (negative for questions
    published in the past, positive for questions that have yet
    to be published).
    """
    time = timezone.now() + timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


def create_choice(question):
    """
    Creates a choice with the given 'choice_text' and assigns it
    to the given 'question'.
    :param question: question choice will be assigned to
    :return: instance of choice object
    """
    return Choice.objects.create(choice_text='choice', question=question)


# Create your tests here.
class QuestionMethodTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return FALSE if
        question was published in the future
        """
        future_question = create_question('text', 30)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() should return FALSE if
        question is more than 1 day old
        """
        for d in range(1, 30):
            time = timezone.now() - timedelta(days=d)
            old_question = Question(pub_date=time)
            self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() should return TRUE if
        question is less than 1 day old
        """
        for h in range(0, 24):
            time = timezone.now() - timedelta(hours=h)
            recent_question = Question(pub_date=time)
            self.assertIs(recent_question.was_published_recently(), True)


class QuestionViewTests(TestCase):
    def test_index_view_with_no_questions(self):
        """
        If no questions exist, an appropriate message should be displayed
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_index_view_with_question_that_has_no_choices(self):
        """
        If question has no choices, we should see the same index as if there
        are no questions.
        """
        create_question(question_text="Past question.", days=-10)
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_index_with_a_past_question(self):
        """
        Questions with a pub_date in the past should be displayed on the
        index page.
        """
        question = create_question(question_text="Past question.", days=-30)
        create_choice(question=question)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_index_view_with_a_future_question(self):
        """
        Questions with pub_date in the future should not be displayed
        on the index page
        """
        question = create_question(question_text="Future Question.", days=30)
        create_choice(question=question)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_index_view_with_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past
        questions should be displayed.
        """
        past_question = create_question(question_text="Past question.", days=-30)
        future_question = create_question(question_text="Future Question.", days=30)
        create_choice(question=past_question)
        create_choice(question=future_question)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_index_view_with_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        first_question = create_question(question_text="Past question 1.", days=-30)
        second_question = create_question(question_text="Past question 2.", days=-5)
        create_choice(question=first_question)
        create_choice(question=second_question)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question 2.>', '<Question: Past question 1.>']
        )


class QuestionIndexDetailTests(TestCase):
    def test_detail_view_with_a_future_question(self):
        """
        The detail view of a questions with a pub_date in the future
        should return a 404 error.
        """
        future_question = create_question(question_text="Future Question.", days=5)
        create_choice(question=future_question)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_detail_view_with_a_past_question(self):
        """
        The detail view of a past question should display the
        question's text.
        """
        past_question = create_question(question_text="Past Question.", days=-5)
        create_choice(question=past_question)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)


class QuestionResultsTests(TestCase):
    def test_results_view_with_a_future_question(self):
        """
        The detail view of a questions with a pub_date in the future
        should return a 404 error.
        """
        future_question = create_question(question_text="Future Question.", days=5)
        url = reverse('polls:results', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_results_view_with_a_past_question(self):
        """
        The detail view of a past question should display the
        question's text.
        """
        past_question = create_question(question_text="Past Question.", days=-5)
        create_choice(past_question)
        url = reverse('polls:results', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)
