
Additional Groups have been added to the system to control

Run the management command:

.. code-block:: bash

	source ~/.venvs/ambition/bin/activate \
	&& cd ~/app \
	&& python manage.py update_edc_permissions

.. code-block:: bash

	python manage.py shell

Add CLINIC group members to PII and RANDO

.. code-block:: python

    from django.contrib.auth.models import User, Group

    pii_group = Group.objects.get(name='PII')
    rando_group = Group.objects.get(name='RANDO')
    for user in User.objects.filter(is_active=True, is_staff=True):
        if 'CLINIC' in [g.name for g in user.groups.all()]:
            user.groups.add(pii_group)
            user.groups.add(rando_group)
            user.save()

