'''
Implementation of the Pk segmentation evaluation metric described in 
[BeefermanBerger1999]_

.. moduleauthor:: Chris Fournier <chris.m.fournier@gmail.com>
'''
from __future__ import division
from decimal import Decimal
from . import compute_window_size, WINDOW_METRIC_DEFAULTS
from ..util import __fnc_metric__, SegmentationMetricError
from ..format import BoundaryFormat, convert_masses_to_positions


def __pk__(hypothesis, reference, window_size, one_minus, boundary_format,
           return_parts, fnc_round):
    '''
    Calculates the Pk segmentation evaluation metric score for a
    hypothetical segmentation against a reference segmentation for a given
    window size.  The standard method of calculating the window size
    is performed if a window size is not specified.
    
    :param hypothesis: Hypothesis segmentation section labels
                                    sequence.
    :param reference:  Reference segmentation section labels sequence.
    :param window_size:          The size of the window that is slid over the \
                                    two segmentations used to count mismatches \
                                    (default is None and will use the average \
                                    window size)
    :param one_minus:            Return 1-Pk to make it no longer a \
                                    penalty-metric.
    :param convert_from_masses:  Convert the segmentations provided from \
                                    masses into positions.
    :type hypothesis: list
    :type reference: list
    :type window_size: int
    :type one_minus: bool
    :type convert_from_masses: bool
    
    .. note:: See :func:`segeval.convert_masses_to_positions` for an example of
              the input format.
    '''
    # pylint: disable=C0103,R0913
    # Convert from masses into positions 
    if boundary_format == BoundaryFormat.mass:
        reference  = convert_masses_to_positions(reference)
        hypothesis = convert_masses_to_positions(hypothesis)
    elif boundary_format != BoundaryFormat.position:
        raise SegmentationMetricError('Unsupported boundary format')
    # Check for input errors
    if len(reference) is not len(hypothesis):
        raise SegmentationMetricError(
                    'Reference and hypothesis segmentations differ in position \
length (%(ref)i is not %(hyp)i).' % {'ref' : len(reference),
                                 'hyp' : len(hypothesis)})
    # Compute window size to use if unspecified
    if window_size is None:
        window_size = compute_window_size(reference, fnc_round,
                                          BoundaryFormat.position)
    # Create a set of pairs of units from each segmentation to go over using a
    # window
    sum_differences = 0
    # Slide window over and sum the number of varying windows
    measurements = 0
    for i in xrange(0, len(reference) - (window_size)):
        # Create probe windows with k boundaries inside
        window_ref = reference[i:i+window_size+1]
        window_hyp = hypothesis[i:i+window_size+1]
        # Probe agreement
        agree_ref = window_ref[0] is window_ref[-1]
        agree_hyp = window_hyp[0] is window_hyp[-1]
        # If the windows agreements agree
        if agree_ref is not agree_hyp:
            sum_differences += 1
        measurements += 1
    # Perform final division
    p_k = Decimal(sum_differences) / measurements
    if not one_minus:
        if return_parts:
            return sum_differences, measurements
        else:
            return p_k
    else:
        return Decimal('1.0') - p_k


def pk(*args, **kwargs):
    # pylint: disable=W0142
    return __fnc_metric__(__pk__, args, kwargs, WINDOW_METRIC_DEFAULTS)

