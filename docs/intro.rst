Introduction
============

**Common Groups** is a project for molecular structure-based classification of
chemical substances into groups with known environmental health hazards.

*This is a work in progress and is not yet stable or viable for general use.*


Goals
-----

Certain *groups* or *classes* of chemical substances are of interest because of
their environmental or toxicological hazard characteristics. Many chemical
groups are referenced in hazard screening methods and named in regulatory
lists.  However, determining the set of specific chemicals that might belong to
each group is usually left up to someone else.

The goal of this project is to provide methods to identify arbitrary sets of
chemicals belonging to structurally-defined classes. We aim to apply basic
cheminformatics techniques to:

-  Find all substances within a larger set (i.e., database) that belong to a
   given group.

-  Classify individual substances into the correct group(s).

-  Perform these functions automatically for a large number of groups all at
   once.

We imagine the possible uses of the project to include answering questions
like: *What dithiocarbamates are in this list of compounds?* or *Does this new
compound belong to any chemical groups associated with endocrine disruption?*


Frequently asked questions
--------------------------

**Does this tool use structural similarity searching?** No, it uses highly
specific substructure searching using `SMARTS`_ and SQL. The idea is that the
groups of chemicals we want to identify are defined by precise criteria, rather
than inferred by similarity. We see this approach as complementary to
similarity searching methods, with each approach having different advantages.

**Does this tool identify toxicophores?** No. Toxicophore identification is
part of the rational basis for identifying groups of substances by structure,
and is therefore a background condition, not a function, of this software.

**Isn't this limited by the current state of knowledge linking individual
groups of chemicals to individual hazard endpoints?** Yes. The purpose of this
project is not to create new knowledge *about* compound groups, but to identify
potentially new *associations* between specific compounds and hazards, based on
existing knowledge.

.. _SMARTS: http://www.daylight.com/dayhtml/doc/theory/theory.smarts.html
