from django.db import models

class MaintenanceLog(models.Model):
    PROJECT_TYPES = [
        ('React', 'React'),
        ('Next.js', 'Next.js'),
        ('WordPress', 'WordPress'),
        # Agrega otros tipos de proyectos si es necesario
    ]

    project_name = models.CharField(max_length=100)
    project_type = models.CharField(max_length=50, choices=PROJECT_TYPES)
    last_review_date = models.DateField()
    responsible = models.CharField(max_length=100)
    general_notes = models.TextField(blank=True)

    update_dependencies = models.BooleanField(default=False)
    check_plugins_themes = models.BooleanField(default=False)
    security_audit = models.BooleanField(default=False)
    check_ssl_certificates = models.BooleanField(default=False)
    review_access_permissions = models.BooleanField(default=False)
    performance_optimization = models.BooleanField(default=False)
    run_tests = models.BooleanField(default=False)
    update_documentation = models.BooleanField(default=False)
    verify_backups = models.BooleanField(default=False)
    monitoring_and_reporting = models.BooleanField(default=False)
    deployment_preparation = models.BooleanField(default=False)

    additional_notes = models.TextField(blank=True)
    pending_tasks = models.TextField(blank=True)

    def __str__(self):
        return self.project_name
