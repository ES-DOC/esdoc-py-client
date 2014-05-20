"""
.. module:: activity_numerical_experiment.py
   :platform: Unix, Windows
   :synopsis: Parses a cim.v1.activity.numerical_experiment document.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
def _set_type_display_name(ctx):
    """Sets document type display name."""
    ctx.meta.type_display_name = ctx.ext.type_display_name = "Experiment"


def _set_full_experiment_name(ctx):
    """Sets full experiment name."""
    name = ""
    if ctx.doc.experiment_id is not None:
    	name += ctx.doc.experiment_id
    	name += " "
    name += ctx.doc.short_name

    ctx.ext.full_experiment_name = name


# Set of parsing functions.
PARSERS = (
    _set_type_display_name,
    _set_full_experiment_name,
    )
