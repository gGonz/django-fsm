from django.db import models
from django_fsm.db.fields import FSMField, FSMKeyField, transition


class Application(models.Model):
    """
    Student application need to be approved by dept chair and dean.
    Test workflow
    """
    state = FSMField(default='new')

    @transition(field=state, source='new', target='draft')
    def draft(self):
        pass

    @transition(field=state, source=['new', 'draft'], target='dept')
    def to_approvement(self):
        pass

    @transition(field=state, source='dept', target='dean')
    def dept_approved(self):
        pass

    @transition(field=state, source='dept', target='new')
    def dept_rejected(self):
        pass

    @transition(field=state, source='dean', target='done')
    def dean_approved(self):
        pass

    @transition(field=state, source='dean', target='dept')
    def dean_rejected(self):
        pass


class FKApplication(models.Model):
    """
    Student application need to be approved by dept chair and dean.
    Test workflow for FSMKeyField
    """
    state = FSMKeyField('testapp.DbState', default='new')

    @transition(field=state, source='new', target='draft')
    def draft(self):
        pass

    @transition(field=state, source=['new', 'draft'], target='dept')
    def to_approvement(self):
        pass

    @transition(field=state, source='dept', target='dean')
    def dept_approved(self):
        pass

    @transition(field=state, source='dept', target='new')
    def dept_rejected(self):
        pass

    @transition(field=state, source='dean', target='done')
    def dean_approved(self):
        pass

    @transition(field=state, source='dean', target='dept')
    def dean_rejected(self):
        pass


class DbState(models.Model):
    '''
    States in DB
    '''
    id = models.CharField(primary_key=True, max_length=50)

    label = models.CharField(max_length=255)

    def __unicode__(self):
        return self.label


class BlogPost(models.Model):
    """
    Test workflow
    """
    state = FSMField(default='new', protected=True)

    @transition(field=state, source='new', target='published')
    def publish(self):
        pass

    @transition(field=state, source='published')
    def notify_all(self):
        pass

    @transition(field=state, source='published', target='hidden')
    def hide(self):
        pass

    @transition(field=state, source='new', target='removed')
    def remove(self):
        raise Exception('No rights to delete %s' % self)

    @transition(field=state, source=['published', 'hidden'], target='stolen')
    def steal(self):
        pass

    @transition(field=state, source='*', target='moderated')
    def moderate(self):
        pass
