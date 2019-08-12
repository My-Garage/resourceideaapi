"""
List of permissions granted to the different groups.
"""
resource_permissions = ['view_clientindustry',
                        'view_client',
                        'view_lineofservice'
                        'view_engagement',
                        'view_job',
                        'view_task',
                        'view_taskassignment']

administrator_permissions = resource_permissions + ['add_employee',
                                                    'change_employee',
                                                    'delete_employee',
                                                    'view_employee',
                                                    'add_clientindustry',
                                                    'change_clientindustry',
                                                    'delete_clientindustry',
                                                    'add_client',
                                                    'change_client',
                                                    'delete_client',
                                                    'add_lineofservice',
                                                    'change_lineofservice',
                                                    'delete_lineofservice',
                                                    'add_engagement',
                                                    'change_engagement',
                                                    'delete_engagement',
                                                    'add_job',
                                                    'change_job',
                                                    'delete_job',
                                                    'add_task',
                                                    'change_task',
                                                    'delete_task',
                                                    'add_taskassignment',
                                                    'change_taskassignment',
                                                    'delete_taskassignment']
